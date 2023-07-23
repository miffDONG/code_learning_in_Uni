using System.Collections;
using System.Collections.Generic;
using System.Runtime.CompilerServices;
using System.Threading;
using UnityEngine;

public class Alien : MonoBehaviour
{
    [SerializeField]
    private AlienSO alienSO;
    [SerializeField]
    private int alienID;
    private AlienItem myAlien;

    [SerializeField]
    private LayerMask targetLayermask;

    protected int health;
    private int moveSpeed;
    private bool isAttacking;
    private bool gotSlow;
    private Vector2 moveDirection = Vector2.left;

    private Animator AlienAnim;

    public Animator GetAlienAnim
    {
        get { return AlienAnim; }
    }

    protected virtual void Start()
    {
        AlienAnim = GetComponent<Animator>();
        myAlien = alienSO.alienItems[alienID];
        
        health = myAlien.health;
        moveSpeed = myAlien.moveSpeed;
        isAttacking = false;
        gotSlow = false;
    }
    

    void Update()
    {
        RaycastHit2D hit = Physics2D.Raycast(transform.position, Vector3.left, myAlien.attackRange, targetLayermask);
        if (hit.collider != null)
        {
            Stop();
            Attack();
        }
        else
        {
            Move();
        }

        /* moveSpeed = 0: Stop, !0: Move */
        transform.Translate(moveDirection * moveSpeed * Time.deltaTime);
    }

    public virtual void TakeDamage(int damage)
    {
        health -= damage;

        if (health <= 0)
        {
            Die();
        }
    }

    protected void Move()
    {
        if (gotSlow) {
            moveSpeed = myAlien.moveSpeed / 2;
        }
        else {
            moveSpeed = myAlien.moveSpeed;
        }
        AlienAnim.SetBool("isAttack",false);
        AlienAnim.SetBool("isMoving", true);
    }

    protected void Stop()
    {
        moveSpeed = 0;
        AlienAnim.SetBool("isMoving",false);
    }

    protected void Die()
    {
        Destroy(gameObject);
        
        CoinManager.instance.IncreaseCoin(myAlien.coin);
    }

    public void getSlow(float slowTime) {
        while (slowTime > 0) {
            gotSlow = true;
            slowTime -= Time.deltaTime;
        }
        gotSlow = false;
    }


    private void Attack()
    {
        if (!isAttacking)
        {
            isAttacking = true;
            StartCoroutine("CreateAttack");
        }
    }

    private IEnumerator CreateAttack()
    {
        yield return new WaitForSeconds(myAlien.attackSpeed);
        GameObject attackPrefab = myAlien.AttackPrefab;
        Instantiate(attackPrefab, new Vector3(transform.position.x, transform.position.y-0.5f, transform.position.z-2), transform.rotation);
        AlienAnim.SetBool("isAttack",true);
        
        // Wait for a short duration before allowing another attack
        isAttacking = false;
    }

}
